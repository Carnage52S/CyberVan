import java.util.Scanner;

public class PasswordStrengthChecker {

    // Method to check if the password contains a digit
    private static boolean containsDigit(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) {
                return true;
            }
        }
        return false;
    }

    // Method to check if the password contains a special character
    private static boolean containsSpecialChar(String password) {
        String specialChars = "!@#$%^&*()-+";
        for (char c : password.toCharArray()) {
            if (specialChars.indexOf(c) != -1) {
                return true;
            }
        }
        return false;
    }

    // Method to evaluate the password strength
    private static String evaluatePasswordStrength(String password) {
        if (password.length() < 12) {
            return "Weak: Password must be at least 12 characters long.";
        } else if (!containsDigit(password)) {
            return "Weak: Password must contain at least one digit.";
        } else if (!containsSpecialChar(password)) {
            return "Weak: Password must contain at least one special character.";
        } else {
            return "Strong Password.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a password to check its strength:");
        String password = scanner.nextLine();

        String strength = evaluatePasswordStrength(password);
        System.out.println(strength);

        scanner.close();
    }
}
