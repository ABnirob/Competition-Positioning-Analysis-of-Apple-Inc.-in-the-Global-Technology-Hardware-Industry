-- =========================================================================
-- DATABASE DEFINITIONS & SCHEMA SETUP
-- Purpose: Setup relational tables for competitive intelligence indicators.
-- Tool: SQL (PostgreSQL, MySQL, SQL Server)
-- =========================================================================

CREATE DATABASE AppleCompetitionPositioning;
USE AppleCompetitionPositioning;

CREATE TABLE competitor_metrics (
    company_name VARCHAR(100) PRIMARY KEY,
    revenue_usd_billions DECIMAL(12, 2) NOT NULL,
    market_cap_usd_billions DECIMAL(12, 2) NOT NULL,
    net_income_usd_billions DECIMAL(12, 2) NOT NULL,
    rd_intensity_percentage DECIMAL(5, 2) NOT NULL,
    operating_margin_percentage DECIMAL(5, 2) NOT NULL,
    employee_productivity_thousands_usd INT NOT NULL,
    market_share_percentage INT NOT NULL,
    brand_score INT NOT NULL,
    innovation_score INT NOT NULL
);

-- Seed values for FY 2024 SCDATA competitive benchmarks
INSERT INTO competitor_metrics (
    company_name, 
    revenue_usd_billions, 
    market_cap_usd_billions, 
    net_income_usd_billions, 
    rd_intensity_percentage, 
    operating_margin_percentage, 
    employee_productivity_thousands_usd, 
    market_share_percentage, 
    brand_score, 
    innovation_score
) VALUES
('Apple', 391.00, 3100.00, 97.00, 7.80, 25.30, 2380, 31, 98, 98),
('Samsung', 222.00, 370.00, 11.40, 11.20, 5.70, 743, 27, 93, 93),
('Dell', 102.00, 95.00, 3.20, 3.10, 4.80, 850, 15, 82, 82),
('Lenovo', 62.00, 15.00, 1.60, 3.20, 3.50, 510, 9, 76, 76),
('HP', 54.00, 32.00, 2.90, 3.00, 5.40, 930, 13, 78, 78);
