import 'dotenv/config';
import axios from 'axios';

export default async (req, res) => {
  try {
    // Make the GET request to the microservice endpoint
    // const response = await axios.get(`${process.env.TOOL_MICRO_SERVICE}/tools`);
    
    // Respond with the data received from the microservice
    res.status(200).json([
        {
            "name": "contrast",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "contrast",
                    "type": "float",
                    "value": 0,
                    "min_value":-100,
                    "max_value":100
                }
            ]
        },
        {
            "name": "border",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "border_width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "border_height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1080
                },
                {
                    "name": "border_color",
                    "type": "hex",
                    "value": "#000000"
                }
            ]
        },
        {
            "name": "brightness",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "brightness",
                    "type": "float",
                    "value": 0,
                    "min_value": -1,
                    "max_value": 1
                }
            ]
        },
        {
            "name": "crop",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1080
                },
                {
                    "name": "x_top_left",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "y_top_left",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "min_value": 1080
                }
            ]
        },
        {
            "name": "ocr",
            "input_type": "image",
            "output_type": "text",
            "parameters": []
        },
        {
            "name": "rotate",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "angle",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 360
                }
            ]
        },
        {
            "name": "scale",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 8
                },
                {
                    "name": "height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 8
                }
            ]
        }
    ]);
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching tools:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch tools',
      details: error.response?.data || error.message,
    });
  }
};
