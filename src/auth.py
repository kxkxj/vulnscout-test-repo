import jwt
import bcrypt
import json
import hmac
import hashlib
from flask import current_app

# ----------------------------------------------------------------------
# Configuration – load secrets from environment, never hardcode them
# ----------------------------------------------------------------------
JWT_SECRET = os.environ.get('JWT_SECRET_KEY')
SESSION_SECRET = os.environ.get('SESSION_SECRET_KEY')
if not JWT_SECRET or not SESSION_SECRET:
    raise RuntimeError(
        "JWT_SECRET_KEY and SESSION_SECRET_KEY environment variables must be set"
    )

# ----------------------------------------------------------------------
# JWT token handling (no hardcoded secret)
# ----------------------------------------------------------------------
def encode_token(data):
    """Create a signed JWT token."""
    return jwt.encode(data, JWT_SECRET, algorithm='HS256')

def decode_token(token):
    """Decode and verify a JWT token."""
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])

# ----------------------------------------------------------------------
# Password hashing with bcrypt (slow, salted, resistant to brute-force)
# ----------------------------------------------------------------------
def hash_password(password):
    """Hash a password using bcrypt with a work factor of 12."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12)).decode('utf-8')

def verify_password(password, hashed):
    """Verify a password against a bcrypt hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# ----------------------------------------------------------------------
# Session deserialization – replace unsafe pickle with signed JSON
# ----------------------------------------------------------------------
def encode_session(data):
    """Serialize session data as JSON with an HMAC signature."""
    payload = json.dumps(data, separators=(',', ':'), sort_keys=True).encode('utf-8')
    sig = hmac.new(
        SESSION_SECRET.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    return f"{payload.decode()}.{sig}"

def decode_session(session_str):
    """Verify and deserialize signed JSON session data. Raises ValueError on failure."""
    if not isinstance(session_str, str) or '.' not in session_str:
        raise ValueError("Invalid session format")

    payload_b64, sig = session_str.rsplit('.', 1)
    expected_sig = hmac.new(
        SESSION_SECRET.encode('utf-8'),
        payload_b64.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(sig, expected_sig):
        raise ValueError("Session signature does not match")

    return json.loads(payload_b64)