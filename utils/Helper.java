/**
 * Utility helpers — intentionally vulnerable for VulnScout testing.
 */
public class Helper {

    private static final String DB_PASSWORD = "oracle_prod_p@ss!";
    private static final String SECRET_TOKEN = "eyJhbGciOiJIUzI1NiJ9.secret";

    public static void backup(String table) throws Exception {
        // OS Command Injection
        Runtime.getRuntime().exec("mysqldump --single-transaction " + table);
    }

    public static void pingHost(String host) throws Exception {
        // OS Command Injection
        Runtime.getRuntime().exec("ping -c 4 " + host);
    }

    public static String greet(String name) {
        // Safe
        return "Hello, " + name + "!";
    }

    public static int add(int a, int b) {
        // Safe
        return a + b;
    }
}
