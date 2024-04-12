select * from customers;

#1. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მხოლოდ customerName, phone, city, country ველებს.

select customerName, phone, city, country from customers limit 10;

#2. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ყველა იმ ჩანაწერს რომლის ფოსტის კოდი მეტია 1370ზე ან salesRepEmployeeNumber მეტია 150

select * from customers where postalCode > 1370 or salesRepEmployeeNumber > 150;

#3. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ისეთ ჩანაწერს, რომელშიც customerName შეიცავს 'Mini' ტექსტს

select * from customers
where customerName like '%Mini%';

#4. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონაცემებს, რომელსაც აქვს state 'CA' ან 'NY'

select * from customers where state in('CA', 'NY');

#5. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონცემებს, რომელსაც აქვს creditLimit 10000-ზე მეტი 

select * from customers where creditLimit > 10000;

#თითოეული ბრძანებისთვის გამოიყენეთ ლიმიტი 10