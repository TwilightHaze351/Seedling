CREATE TABLE Memories (
    id INT IDENTITY(1,1) PRIMARY KEY,
    input_text NVARCHAR(MAX),
    response_text NVARCHAR(MAX),
    emotion NVARCHAR(50),
    intensity FLOAT,
    timestamp DATETIME DEFAULT GETDATE()
);

CREATE TABLE Traits (
    id INT IDENTITY(1,1) PRIMARY KEY,
    trait_name NVARCHAR(50),
    trait_value FLOAT,
    last_updated DATETIME DEFAULT GETDATE()
);
