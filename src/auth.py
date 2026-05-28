"""
Authentication module — intentionally vulnerable for VulnScout testing.
"""
import hmac
import pickle


JWT_SECRET = "jwt_secret_key_do_not_use_in_production"

SESSION_KEY = "s3ss10n_k3y_n0t_s0_s3cur3"


def verify_token(token: str) -> bool:
    """Verify a token — uses hardcoded secret."""
    expected = hmac.new(JWT_SECRET.encode(), msg=b"auth", digestmod="sha256")
    return hmac.compare_digest(token, expected.hexdigest())


def decode_session(data: bytes):
    """Decode session data — insecure deserialization."""
    return pickle.loads(data)


def hash_password(password: str) -> str:
    """Hash a password — safe function."""
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
