-- Table for distinct device types
CREATE TABLE device_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);
 
 
CREATE TABLE ticket (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(255) NOT NULL,
    -- device_type is now derived from the device table
    status VARCHAR(50) NOT NULL DEFAULT 'Open', -- Added default status
    description TEXT,
    assigned_to_technician_id INT,
    priority VARCHAR(20) DEFAULT 'Medium', -- e.g., Low, Medium, High, Critical
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_ticket_device
        FOREIGN KEY(device_id)
        REFERENCES device(device_id),
    CONSTRAINT fk_technician
        FOREIGN KEY(assigned_to_technician_id)
        REFERENCES service_technician(technician_id)
);
 
CREATE TABLE device (
    device_id VARCHAR(255) PRIMARY KEY,
    device_type_id INT NOT NULL,
    friendly_name VARCHAR(255),
    location VARCHAR(255),
    status VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_device_devicetype
        FOREIGN KEY(device_type_id)
        REFERENCES device_type(id)
);
 
CREATE TABLE service_technician (
    technician_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(20),
    specialization_device_type_id INT, -- Technician's specialization, linked to a device type
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_technician_specialization
        FOREIGN KEY(specialization_device_type_id)
        REFERENCES device_type(id)
);
 
-- Sample data for device_type
INSERT INTO device_type (name, description) VALUES
('Furnace', 'Residential and commercial heating furnaces'),
('HVAC Unit', 'Heating, Ventilation, and Air Conditioning units');
 
-- Sample data for device (assuming the device_type IDs are 1 for Furnace, 2 for HVAC Unit after insertion)
-- You might need to adjust device_type_id if your SERIAL sequence starts differently or if you have existing data.
INSERT INTO device (device_id, device_type_id, friendly_name, location, status) VALUES
('FURNACE-SN001', 1, 'Main Building Furnace A', 'Basement - Sector 1', 'online'),
('FURNACE-SN002', 1, 'Annex Furnace Alpha', 'Annex - Utility Closet', 'offline'),
('HVAC-SN001', 2, 'Rooftop HVAC Unit 1', 'Rooftop - East Wing', 'online'),
('HVAC-SN002', 2, 'Ground Floor HVAC', 'Ground Floor - West Wing', 'maintenance');
 
-- Sample data for service_technician
INSERT INTO service_technician (first_name, last_name, email, phone_number, specialization_device_type_id, is_active) VALUES
('John', 'Smith', 'john.smith@example.com', '555-0101', 1, TRUE), -- Specializes in Furnaces
('Alice', 'Brown', 'alice.brown@example.com', '555-0102', 2, TRUE), -- Specializes in HVAC Units
('Bob', 'Johnson', 'bob.johnson@example.com', '555-0103', 1, TRUE); -- Also specializes in Furnaces



-- Ticket 1: Open, assigned to John Smith, for Main Building Furnace A
INSERT INTO ticket (device_id, status, description, assigned_to_technician_id, priority)
VALUES ('FURNACE-SN001', 'Open', 'Furnace not heating properly', 1, 'High');

-- Ticket 2: Closed, assigned to Bob Johnson, for Annex Furnace Alpha
INSERT INTO ticket (device_id, status, description, assigned_to_technician_id, priority)
VALUES ('FURN-T-001', 'Closed', 'Furnace was offline, reset performed', 3, 'Medium');

-- Ticket 3: Open, assigned to Alice Brown, for Rooftop HVAC Unit 1
INSERT INTO ticket (device_id, status, description, assigned_to_technician_id, priority)
VALUES ('HVAC-SN001', 'Open', 'HVAC unit making loud noise', 2, 'Critical');

-- Ticket 4: Open, unassigned, for Ground Floor HVAC
INSERT INTO ticket (device_id, status, description, priority)
VALUES ('HVAC-SN002', 'Open', 'Routine maintenance required', 'Low');