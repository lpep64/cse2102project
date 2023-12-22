onst uri = 'https://g0fzaxfewh.execute-api.us-east-1.amazonaws.com/beta?operation=add_course';

  const headers = {
    'Content-Type': 'application/json',
    'x-amz-docs-region': 'us-east-1'
  };

  const para = {
    "operation": "add_course",
    "name": "CSE 3500",
    "description": "Algorithms and Complexity",
    "secdatetime": ["1.M110:11,W10:11,F10:11", "2.Tu8:10,Th8:10"],
    "students": ["2976926"],
    "teachers": ["1111111","1111113"]
  }

  fetch(uri, {
    method: 'OPTIONS',
    headers: headers,
    body: JSON.stringify(para)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.text();  // First get the text of the response
  })
  .then(text => {
    try {
      return JSON.parse(text);  // Then try to parse it as JSON
    } catch (error) {
      console.error('Parsing error:', error);
      throw new Error(`Invalid JSON: ${text}`);
    }
  })
  .then(data => {
    // Use the data
  })
  .catch(error => {
    console.error('There was an error!', error);
  });
}