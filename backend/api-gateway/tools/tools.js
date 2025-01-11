import 'dotenv/config';
import axios from 'axios';

export default async (req, res) => {
  try {
    // Make the GET request to the microservice endpoint
    const response = await axios.get(`${process.env.TOOL_MICRO_SERVICE}/tools`);
    
    // Respond with the data received from the microservice
    res.status(200).json(response.data);
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching tools:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch tools',
      details: error.response?.data || error.message,
    });
  }
};
