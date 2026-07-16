-- =========================================================================
-- CORE SQL ANALYTIC QUERIES
-- Purpose: Extract executive insights and performance gaps.
-- =========================================================================

-- Query 1: Enterprise Performance Ranking (Sort by Revenue vs. Market Cap)
SELECT 
    RANK() OVER (ORDER BY revenue_usd_billions DESC) AS revenue_rank,
    company_name,
    revenue_usd_billions,
    market_cap_usd_billions,
    operating_margin_percentage
FROM competitor_metrics;

-- Query 2: Operating margin and employee productivity delta
SELECT 
    company_name,
    operating_margin_percentage,
    operating_margin_percentage - (SELECT AVG(operating_margin_percentage) FROM competitor_metrics) AS margin_delta_from_avg,
    employee_productivity_thousands_usd,
    employee_productivity_thousands_usd - (SELECT AVG(employee_productivity_thousands_usd) FROM competitor_metrics) AS productivity_delta_from_avg
FROM competitor_metrics
ORDER BY operating_margin_percentage DESC;

-- Query 3: Multi-weighted Overall Competitive Score Calculation
-- Formula weights: 40% Operating Margin, 30% Brand, 30% Innovation Index
SELECT 
    company_name,
    operating_margin_percentage,
    brand_score,
    innovation_score,
    ROUND(
        (operating_margin_percentage * 100 / 30 * 0.40) + 
        (brand_score / 100.0 * 30 * 0.30) + 
        (innovation_score / 100.0 * 30 * 0.30), 2
    ) AS overall_competitive_score
FROM competitor_metrics
ORDER BY overall_competitive_score DESC;
