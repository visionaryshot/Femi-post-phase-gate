import java.util.Scanner;
public class Library {
public static void main(String[] args) {
 Scanner scanner = new Scanner(System.in);

        String[] bookTitles = {
            "Harry Potter", "The Hobbit", "To Kill a Mockingbird", "1984", "Pride and Prejudice"
        };
        String[] bookReport = {
            "available", "available", "available", "available", "available"
        };

        int userInput;

        do {
            
            System.out.println("\nDASHBOARD");
            System.out.println("1. View all books");
            System.out.println("2. Borrow a book");
            System.out.println("3. Return a book");
            System.out.println("4. Exit");
            System. out.print("Enter your choice (1-4): ");
            userInput= scanner.nextInt();
            scanner.nextLine(); 
            switch (userInput) {
                case 1:
                    viewAllBooks(bookTitles, bookReport);
                    break;
                case 2:
                    borrowBook(bookTitles, bookReport, scanner);
                    break;
                case 3:
                    returnBook(bookTitles, bookReport, scanner);
                    break;
                case 4:
                    System.out.println("Have a nice day buddy!");
                    break;
                default:
                    System.out.println("Wrong input. Choose between 1-4.");
}
} while (userInput!= 4);

        scanner.close();
}

    public static void viewAllBooks(String[] titles, String[] report) {
    System.out.println("\nALL BOOKS");
     for (int count = 0; count < titles.length; count++) {
      System.out.println((count + 1) + ". " + titles[count ] + " - " + report[count]);
}
}

    public static void borrowBook(String[] titles, String[] report, Scanner scanner) {
     System.out.println("\nBORROW A BOOK");
     int availableCount = 0;

     for (int count  = 0; count  < titles.length; count++) {
      if (report[count].equals("available")) {
      System.out.println((count  + 1) + ". " + titles[count]);
      availableCount++;
}
}

        if (availableCount == 0) {
         System.out.println("No books available to borrow.");
         return;
}

        System.out.print("Enter the book number to borrow: ");
        int bookNumber = scanner.nextInt();
        scanner.nextLine();

        if (bookNumber >= 1 && bookNumber <= titles.length) {
        if (report[bookNumber - 1].equals("available")) {
        report[bookNumber - 1] = "borrowed";
        System.out.println("You have borrowed '" + titles[bookNumber - 1] + "'");
         } else {
        System.out.println("This book is not available.");
}
} else {
System.out.println("Invalid book number.");
}
}

    public static void returnBook(String[] titles, String[] report, Scanner scanner) {
     System.out.println("\nRETURN A BOOK");
     int borrowedCount = 0;

        for (int count  = 0; count  < titles.length; count++) {
         if (report[count ].equals("borrowed")) {
        System.out.println((count + 1) + ". " + titles[count]);
         borrowedCount++;
}
}

        if (borrowedCount == 0) {
        System.out.println("No books are currently borrowed.");
         return;
}

        System.out.print("Enter the book number to return: ");
        int bookNumber = scanner.nextInt();
        scanner.nextLine();

        if (bookNumber >= 1 && bookNumber <= titles.length) {
        if (report[bookNumber - 1].equals("borrowed")) {
         report[bookNumber - 1] = "available";
         System.out.println("You have returned '" + titles[bookNumber - 1] + "'");
         } else {
         System.out.println("This book was not borrowed.");
          }
 } else {
      System.out.println("Invalid book number.");
}
}
}
