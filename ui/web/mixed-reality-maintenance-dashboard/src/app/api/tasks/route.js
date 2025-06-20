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
    "id": 1,
    "title": "Critical Over-Temperature Alert for furnace_1",
    "description": "Jira ID: MACHINECAP-23. Temperature exceeded critical threshold in furnace_1. Immediate action required.",
    "assigned_to": "Technician John Doe",
    "status": "open",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T10:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Over-Temperature",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 2,
    "title": "Critical Anomaly Detected on furnace_1",
    "description": "Jira ID: MACHINECAP-24. Anomaly detected in furnace_1 operation parameters. Investigation needed.",
    "assigned_to": "Technician Jane Smith",
    "status": "in_progress",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T12:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Operational Anomaly",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 3,
    "title": "Critical Over-Temperature Anomaly Detected in furnace_1",
    "description": "Jira ID: MACHINECAP-25. Critical over-temperature anomaly detected, furnace_1 requires immediate inspection.",
    "assigned_to": "Technician Alice Brown",
    "status": "open",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T11:30:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Over-Temperature",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 4,
    "title": "High Temperature Excursion during Preheat phase.",
    "description": "Jira ID: MACHINECAP-26. Temperature excursion above limits during preheat phase detected.",
    "assigned_to": "Technician Bob Johnson",
    "status": "open",
    "priority": "high",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T09:45:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Temperature Excursion",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 5,
    "title": "Critical High Temperature Excursion - furnace_1",
    "description": "Jira ID: MACHINECAP-27. Critical high temperature excursion detected in furnace_1, urgent response needed.",
    "assigned_to": "Technician David Chen",
    "status": "in_progress",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T10:15:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "High Temperature Excursion",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 6,
    "title": "Critical Over-Temperature Alert for furnace_1",
    "description": "Jira ID: MACHINECAP-28. Repeated over-temperature alert for furnace_1, monitoring closely.",
    "assigned_to": "Technician John Doe",
    "status": "open",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T13:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Over-Temperature",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 7,
    "title": "Critical Anomaly Detected on furnace_1",
    "description": "Jira ID: MACHINECAP-29. Unexpected anomaly detected in furnace_1 sensor readings.",
    "assigned_to": "Technician Alice Brown",
    "status": "open",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T14:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Sensor Anomaly",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 8,
    "title": "Critical Over-Temperature Anomaly Detected in furnace_1",
    "description": "Jira ID: MACHINECAP-30. Critical temperature anomaly detected, furnace_1 operation compromised.",
    "assigned_to": "Technician Bob Johnson",
    "status": "in_progress",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T15:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Over-Temperature",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 9,
    "title": "High Temperature Excursion during Preheat phase.",
    "description": "Jira ID: MACHINECAP-31. High temperature excursion detected during preheat phase, verify controls.",
    "assigned_to": "Technician David Chen",
    "status": "open",
    "priority": "high",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T16:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "Temperature Excursion",
    "equipment_id": "FURNACE-1"
  },
  {
    "id": 10,
    "title": "Critical High Temperature Excursion - furnace_1",
    "description": "Jira ID: MACHINECAP-32. Critical high temperature excursion detected, immediate shutdown recommended.",
    "assigned_to": "Technician Jane Smith",
    "status": "open",
    "priority": "critical",
    "location": "Furnace_1 - Plant A",
    "due_date": "2024-06-10T17:00:00Z",
    "department": "Mechanical Maintenance",
    "anomaly_type": "High Temperature Excursion",
    "equipment_id": "FURNACE-1"
  }
];

  return tasks;
}
