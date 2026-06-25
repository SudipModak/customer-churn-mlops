CREATE TABLE upload_history (
    upload_id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    total_records INT,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE customer_uploads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    upload_id INT,
    customer_id VARCHAR(100),
    raw_data JSON
);
CREATE TABLE prediction_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    upload_id INT,
    customer_id VARCHAR(100),
    prediction INT
);