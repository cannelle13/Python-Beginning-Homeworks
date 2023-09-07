from src.bank import Bank, SavingsAccount, CurrentAccount
import unittest
from unittest.mock import patch


class TestBank(unittest.TestCase):
    def test_open_account(self):
        bank = Bank()
        account_number = "test123"
        initial_balance = 0.0

        # Open an account
        bank.open_account(account_number)

        # Find the opened account by account number
        opened_account = None
        for account in bank.accounts:
            if account.get_account_number() == account_number:
                opened_account = account
                break

        # Check if the account was opened and added to the bank's accounts
        self.assertIsNotNone(opened_account)

        # Check if the opened account has the initial balance
        self.assertEqual(opened_account.get_balance(), initial_balance)

    def test_update_savings_account(self):
        bank = Bank()

        # Create a SavingsAccount with initial balance and interest
        savings_account = SavingsAccount(1000.0, "6789", 0.02)
        bank.add_account(savings_account)

        # Update the bank's accounts
        bank.update_account()

        # Check if the interest was added to the account
        self.assertAlmostEqual(
            savings_account.get_balance(), 1000.00 + (1000.00 * 0.02), places=2
        )

    @patch("builtins.print")
    def test_update_current_account(self, mock_print):
        bank = Bank()

        # Create a CurrentAccount with initial balance and overdraft limit
        current_account = CurrentAccount(-2000.0, "76543", 500.00)
        bank.add_account(current_account)

        # Update the bank's accounts
        bank.update_account()

        # Check if the correct message was printed for overdraft
        expected_message = "Letter sent to account. Overdraft exceeded!"
        mock_print.assert_any_call(expected_message)

        # Showing what is in mock in console
        import sys

        sys.stdout.write(str(mock_print.call_args_list) + "\n")


if __name__ == "__main__":
    unittest.main()
