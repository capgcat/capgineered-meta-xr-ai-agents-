import { NextResponse } from 'next/server';

export async function GET() {
  try {
    // Call the Python agent API
    const response = await fetch('http://localhost:5000/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // body: JSON.stringify({ user_input: 1 }), // Query for top 10 tasks
      // body: JSON.stringify({ user_input: "Can you give top 10 tasks in JSON format, Append fourseasons schema name for each query? Return data should be in JSON serializable format in all case" }), // Query for top 10 tasks
      // body: JSON.stringify({ user_input: "Can you give top 10 tasks with fourseasons schema in JSON Object which contains json Array  without object name?" }), // Query for top 10 tasks    
      body: JSON.stringify({ user_input: "Give me all tasks that are pending. Output in json" }), // Query for top 10 tasks    
    });

    console.log("Agent API response status:", response.status);

    if (!response.ok) {
      throw new Error(`Agent API responded with status: ${response.status}`);
    }

    // Parse the agent's response as JSON
    const agentResponseText = await response.text();
    console.log("Agent API response text received.", agentResponseText, " ------------------------  \n\n\n ");
    // console.log();

    // The agent might return a JSON string in its response text
    // We need to parse that string to get the actual tasks data
    try {
      // Try to parse the entire response as JSON first

      // Extract the JSON part from the input
      const jsonString = extractJson(agentResponseText);
      let parsedData; // Declare parsedData outside the if block
      if (jsonString) {
        // Trim the JSON string to remove any leading or trailing whitespace
        parsedData = JSON.parse(jsonString.trim());
        console.log("Parsed agent response:", parsedData);
      } else {
        throw new Error("No valid JSON found in the input.");
      }
      // If successful, check if it's in the format we expect
      if (Array.isArray(parsedData)) {
        return NextResponse.json(parsedData);
      } else if (parsedData.data && Array.isArray(parsedData.data)) {
        const columns = parsedData.columns;
        const tasks = parsedData.data.map(row => {
          const task = {};
          columns.forEach((col, i) => {
            task[col] = row[i];
          });
          return task;
        });
        return NextResponse.json(tasks);
      } else {
        // If there's specific JSON within the text, we need to extract and parse it
        // This is a fallback approach
        console.log("Unexpected data structure, returning original response");
        return NextResponse.json(parsedData);
      }
    } catch (parseError) {
      console.error("Error parsing agent response:", parseError);

      // Fallback to the mock data if we can't parse the agent response
      return NextResponse.json(getMockTasks());
    }
  } catch (error) {
    console.error("Error fetching from agent API:", error);

    // If the agent API is unavailable, use the mock data
    return NextResponse.json(getMockTasks());
  }
}

// Function to extract valid JSON from the input string
function extractJson(input) {
  try {
    // Attempt to find and parse the first valid JSON object or array
    const startIndex = input.indexOf('{');
    const endIndex = input.lastIndexOf('}');
    if (startIndex !== -1 && endIndex !== -1) {
      const jsonString = input.substring(startIndex, endIndex + 1);
      return JSON.parse(jsonString); // Parse and return the JSON object
    }
  } catch (error) {
    console.error("Error extracting JSON:", error);
  }
  return null; // Return null if no valid JSON is found
}

function getMockTasks() {
  // Get date references for last week, today, and next week
  const today = new Date();

  // Format a date to ISO string with time
  const formatDate = (date) => {
    return date.toISOString().split('.')[0]; // Remove milliseconds
  };

  function getTimeForToday(hour, minute = 0) {
    // Create a date for today
    const date = new Date();
    
    // Get timezone offset in minutes
    const tzOffset = date.getTimezoneOffset();
    
    // Set the date to today with the specified local time
    date.setHours(hour, minute, 0, 0);
    
    // Adjust for timezone to ensure the time is interpreted as local time
    // We need to subtract the offset because getTimezoneOffset returns minutes WEST of UTC
    const adjustedDate = new Date(date.getTime() - tzOffset * 60000);
    
    // Format as ISO string without milliseconds
    const formattedDate = adjustedDate.toISOString().split('.')[0];
    
    console.log(`Formatted date for ${hour}:${minute === 0 ? '00' : minute}: ${formattedDate}`);
    return formattedDate;
  }

  // Helper to get a date with an offset from today
  const getOffsetDate = (dayOffset, hourOffset = 0) => {
    const date = new Date();
    date.setDate(date.getDate() + dayOffset);
    date.setHours(date.getHours() + hourOffset);
    return formatDate(date);
  };

  // Get dates for various offsets
  const yesterday = getOffsetDate(-1);
  const todayDate = getOffsetDate(0, 3); // 3 hours from now
  const tomorrow = getOffsetDate(1);
  const twoDaysAgo = getOffsetDate(-2);
  const threeDaysAgo = getOffsetDate(-3);
  const fourDaysAgo = getOffsetDate(-4);
  const fiveDaysAgo = getOffsetDate(-5);
  const threeDaysFromNow = getOffsetDate(3);
  const fourDaysFromNow = getOffsetDate(4);
  const fiveDaysFromNow = getOffsetDate(5);
  const sixDaysFromNow = getOffsetDate(6);

  // Simulating database data
  const tasks = [
  {
    id: 1,
    title: 'Overheating Detected: Compressor Unit A3',
    description: 'Temperature sensor reports overheating above threshold. Immediate inspection required.',
    assigned_to: 'Technician Jane Smith',
    assigned_to_id: 2,
    status: 'in_progress',
    priority: 'high',
    location: 'Compressor Unit A3 - Plant 1',
    due_date: new Date(Date.now() + 2 * 60 * 60 * 1000), // 2 hours from now
    department: 'Mechanical Maintenance',
    anomaly_type: 'Overheating',
    equipment_id: 'EQP-A3'
  },
  {
    id: 2,
    title: 'Vibration Anomaly: Conveyor Belt B7',
    description: 'Vibration levels exceed safe limits. Possible misalignment or worn bearings.',
    assigned_to: 'Technician David Chen',
    assigned_to_id: 3,
    status: 'open',
    priority: 'critical',
    location: 'Conveyor Belt B7 - Assembly Line 2',
    due_date: new Date(Date.now() + 1 * 60 * 60 * 1000), // 1 hour from now
    department: 'Production Maintenance',
    anomaly_type: 'Vibration',
    equipment_id: 'EQP-B7'
  },
  {
    id: 3,
    title: 'Routine Inspection: HVAC Unit 4',
    description: 'Scheduled preventive maintenance for HVAC filters and coolant levels.',
    assigned_to: 'Technician Alice Brown',
    assigned_to_id: 4,
    status: 'scheduled',
    priority: 'medium',
    location: 'HVAC Unit 4 - Admin Block',
    due_date: new Date(Date.now() + 24 * 60 * 60 * 1000), // 24 hours from now
    department: 'Facility Management',
    anomaly_type: 'Preventive',
    equipment_id: 'HVAC-4'
  },
  {
    id: 4,
    title: 'Low Battery Alert: Sensor Node S12',
    description: 'Battery level below 10%. Replace battery to avoid data loss.',
    assigned_to: 'Technician Bob Johnson',
    assigned_to_id: 5,
    status: 'open',
    priority: 'high',
    location: 'Sensor Node S12 - Warehouse 3',
    due_date: new Date(Date.now() + 3 * 60 * 60 * 1000), // 3 hours from now
    department: 'IoT Maintenance',
    anomaly_type: 'Low Battery',
    equipment_id: 'SNS-S12'
  },
  {
    id: 5,
    title: 'Current Spike: Pump Station P2',
    description: 'Unexpected current spike detected. Possible short circuit or overload.',
    assigned_to: 'Technician Jane Smith',
    assigned_to_id: 2,
    status: 'in_progress',
    priority: 'critical',
    location: 'Pump Station P2 - Utility Area',
    due_date: new Date(Date.now() + 30 * 60 * 1000), // 30 minutes from now
    department: 'Electrical Maintenance',
    anomaly_type: 'Current Spike',
    equipment_id: 'PUMP-P2'
  },
  {
    id: 6,
    title: 'Humidity Anomaly: Cleanroom CR1',
    description: 'Humidity sensor reports abnormal values. Check for leaks or HVAC malfunction.',
    assigned_to: 'Technician Alice Brown',
    assigned_to_id: 4,
    status: 'open',
    priority: 'medium',
    location: 'Cleanroom CR1 - Lab Wing',
    due_date: new Date(Date.now() + 4 * 60 * 60 * 1000), // 4 hours from now
    department: 'Facility Management',
    anomaly_type: 'Humidity',
    equipment_id: 'CR1'
  },
  {
    id: 7,
    title: 'Sensor Offline: Furnace F1',
    description: 'No data received from temperature sensor. Possible sensor failure or connectivity issue.',
    assigned_to: null,
    assigned_to_id: null,
    status: 'open',
    priority: 'high',
    location: 'Furnace F1 - Foundry',
    due_date: new Date(Date.now() + 2 * 60 * 60 * 1000), // 2 hours from now
    department: 'Mechanical Maintenance',
    anomaly_type: 'Sensor Offline',
    equipment_id: 'FURNACE-F1'
  },
  {
    id: 8,
    title: 'Routine Maintenance: Hydraulic Press HP5',
    description: 'Monthly checkup for hydraulic fluid and pressure calibration.',
    assigned_to: 'Technician David Chen',
    assigned_to_id: 3,
    status: 'scheduled',
    priority: 'low',
    location: 'Hydraulic Press HP5 - Workshop',
    due_date: new Date(Date.now() + 72 * 60 * 60 * 1000), // 3 days from now
    department: 'Mechanical Maintenance',
    anomaly_type: 'Preventive',
    equipment_id: 'HP5'
  },
  {
    id: 9,
    title: 'Overload Warning: Motor M9',
    description: 'Motor current exceeds rated value. Inspect for mechanical blockage.',
    assigned_to: 'Technician Bob Johnson',
    assigned_to_id: 5,
    status: 'in_progress',
    priority: 'high',
    location: 'Motor M9 - Packaging Line',
    due_date: new Date(Date.now() + 1.5 * 60 * 60 * 1000), // 1.5 hours from now
    department: 'Electrical Maintenance',
    anomaly_type: 'Overload',
    equipment_id: 'MOTOR-M9'
  },
  {
    id: 10,
    title: 'Resolved: Vibration Issue - Conveyor Belt B7',
    description: 'Vibration anomaly resolved after bearing replacement.',
    assigned_to: 'Technician David Chen',
    assigned_to_id: 3,
    status: 'closed',
    priority: 'medium',
    location: 'Conveyor Belt B7 - Assembly Line 2',
    due_date: new Date(Date.now() - 2 * 60 * 60 * 1000), // 2 hours ago
    department: 'Production Maintenance',
    anomaly_type: 'Vibration',
    equipment_id: 'EQP-B7'
  }
];

  return tasks;
}
