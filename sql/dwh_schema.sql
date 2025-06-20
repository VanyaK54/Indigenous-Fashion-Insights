-- dwh_schema.sql
-- Dimensional warehouse schema for Indigenous Fashion Insights

-- 🔸 Date Dimension
CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    weekday_name VARCHAR(10),
    is_weekend BOOLEAN
);

-- 🔸 Region Dimension
CREATE TABLE dim_region (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100),
    province_or_state VARCHAR(100),
    country VARCHAR(50)
);

-- 🔸 Pattern Dimension
CREATE TABLE dim_pattern (
    pattern_id SERIAL PRIMARY KEY,
    pattern_name VARCHAR(100),
    culture VARCHAR(100),
    primary_colors TEXT
);

-- 🔸 Sales Fact Table
CREATE TABLE fact_sales (
    sale_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES dim_date(date_id),
    region_id INT REFERENCES dim_region(region_id),
    pattern_id INT REFERENCES dim_pattern(pattern_id),
    units_sold INT,
    price_per_unit DECIMAL(10, 2),
    revenue DECIMAL(12, 2)
);

-- 🔸 Forecast Table (optional)
CREATE TABLE fact_forecast (
    forecast_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES dim_date(date_id),
    pattern_id INT REFERENCES dim_pattern(pattern_id),
    predicted_units INT,
    prediction_source VARCHAR(50) -- e.g., 'RF Model', 'Prophet'
);
