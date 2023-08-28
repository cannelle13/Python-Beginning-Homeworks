#### HW: Testing

1. Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method. Ensure that the account is opened and has balance.
2. Test update method. It should check that code added interest and sent a message (print function was called).


#### Task from 14 lesson
Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.
Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some of each type).

Write an update method in the Bank class. It iterates through each account, updating it in the following ways: Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).
The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.