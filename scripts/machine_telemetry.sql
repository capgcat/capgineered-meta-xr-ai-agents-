CREATE TABLE `your_gcp_project_id.machine_telemetry.raw_observations`
(
    -- Core Identifiers & Timestamp
    `timestamp`                      TIMESTAMP NOT NULL OPTIONS(description="Timestamp when the observation was recorded (UTC)."),
    `machine_id`                     STRING    NOT NULL OPTIONS(description="Unique identifier for the machine."),
    `observation_type`               STRING    NOT NULL OPTIONS(description="Categorization of the observation (e.g., 'temperature_reading', 'pressure_reading', 'vibration_magnitude', 'current_draw', 'flow_rate', 'rpm', 'gauge_reading', 'indicator_light_status', 'component_visual_state')."),
    `sensor_id`                      STRING    NOT NULL OPTIONS(description="Specific identifier for the individual sensor or component (e.g., 'temp_sensor_1', 'motor_vibration_sensor', 'pressure_gauge_PMP001', 'status_light_MOTOR002', 'bearing_housing_front')."),

    -- Numeric Readings (for physical sensors or extracted gauge values)
    `numeric_value`                  FLOAT64           OPTIONS(description="The numeric value of the observation (e.g., temperature in C, pressure in PSI, RPM, numerical gauge reading). NULL if observation_type is non-numeric."),
    `unit`                           STRING            OPTIONS(description="Unit of the numeric_value (e.g., 'Celsius', 'PSI', 'Amps', 'RPM'). NULL if not applicable."),

    -- Categorical/String Readings (for visual observations like light colors, or general component state)
    `string_value`                   STRING            OPTIONS(description="A string value for categorical observations (e.g., 'red', 'green', 'on', 'off' for indicator lights; 'clean', 'dirty', 'cracked', 'ok' for visual component states). NULL if numeric."),

    -- Source Information
    `data_source`                    STRING    NOT NULL OPTIONS(description="Origin of the data (e.g., 'physical_sensor_gateway', 'visual_inspection_agent')."),
    `source_metadata`                JSON              OPTIONS(description="Optional JSON field for source-specific metadata (e.g., device IP, sensor serial number, vision model version)."),

    -- Visual Observation Specific Fields (NULL for non-visual data)
    `image_url`                      STRING            OPTIONS(description="Google Cloud Storage URL to the source image if data originated from a visual inspection agent."),
    `bounding_box_coordinates`       STRING            OPTIONS(description="JSON string representing bounding box coordinates [x, y, width, height] for detected objects/features in the image. NULL if not vision-related."),
    `observation_confidence`         FLOAT64           OPTIONS(description="Confidence score for the visual observation (e.g., confidence in OCR reading, confidence in identifying a specific object/state). NULL if not applicable."),
    `visual_details`                 JSON              OPTIONS(description="Optional JSON for additional raw visual details (e.g., detected color properties, specific feature descriptors).")
)
PARTITION BY DATE(`timestamp`) -- Partition by date for efficient time-series queries
CLUSTER BY `machine_id`, `observation_type` -- Cluster by common query dimensions
OPTIONS(
  description="Raw telemetry and visual observations from machines, serving as input for anomaly detection."
);