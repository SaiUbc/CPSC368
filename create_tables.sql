-- Drop tables if they already exist
DROP TABLE telehealth CASCADE CONSTRAINTS;
DROP TABLE mortality CASCADE CONSTRAINTS;

-- Create the Telehealth table
CREATE TABLE telehealth (
    ID NUMBER PRIMARY KEY,
    Year NUMBER,
    Age_Group VARCHAR2(200),
    State VARCHAR2(200),
    Medicare_Medicaid_Status VARCHAR2(200),
    Race VARCHAR2(200),
    Sex VARCHAR2(200),
    Medicare_Enrollment_Status VARCHAR2(200),
    Age_Grouping VARCHAR2(200),
    Urban_Rural_Description VARCHAR2(200),
    Total_Eligible_Users NUMBER,
    Total_Medicare_Enrollment NUMBER,
    Total_Telehealth_Users NUMBER,
    Percentage_of_Medicare_Telehealth_Users NUMBER
);

-- Create the Mortality table
CREATE TABLE mortality (
    ID NUMBER PRIMARY KEY,
    Year NUMBER,
    Sex VARCHAR2(200),
    Age NUMBER,
    Deaths NUMBER,
    Age_Group VARCHAR2(200)
);
