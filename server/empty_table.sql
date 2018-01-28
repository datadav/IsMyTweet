CREATE TABLE IF NOT EXISTS users (
    ID int PRIMARY KEY,
    Name_Twitter varchar(255) NOT NULL,
    Avatar text NOT NULL,
    Email varchar(255) NOT NULL UNIQUE,
    Id_Last_Tweet int,
    Creation_Date date,
    Notification_By_Mail int
);