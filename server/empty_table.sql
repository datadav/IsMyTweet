CREATE TABLE IF NOT EXISTS users (
    ID int PRIMARY KEY,
    ID_Twitter int NOT NULL,
    Name_Twitter varchar(255),
    Avatar text NOT NULL,
    Email varchar(255) NOT NULL UNIQUE,
    Id_Last_Tweet int,
    Creation_Date date,
    Notification_By_Mail int
);