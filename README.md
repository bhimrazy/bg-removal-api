<div align="center">
<h1>Deploy Background Removal API with LitServe</h1>

<p>Instantly remove image backgrounds with our powerful API, seamlessly deployed using LitServe.
Fast, reliable, and easy to integrate—perfect for any application needing quick background removal.</p>

<a target="_blank" href="https://lightning.ai/bhimrajyadav/studios/deploy-background-removal-api-with-litserve">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/>
</a>

</div>

![image](https://github.com/user-attachments/assets/a9a195b3-8fab-4e84-957e-9a522aa83ad4)


## Getting Started

Follow these steps to set up and run the project:

### 1. Install Dependencies

Ensure all necessary packages are installed by running:

```bash
pip install -r requirements.txt
```

### 2. Start the API Server

Launch the API server powered by [LitServe](https://github.com/Lightning-AI/LitServe):

```bash
python server.py
```

### 3. Test with the Client
Send an image to the server for background removal using the client script:

```bash
python client.py -i thor.jpg -o output.jpg
```

## About

This project is developed and maintained with ❤️ by [Bhimraj Yadav](https://github.com/bhimrazy).