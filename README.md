# DASH Video Streaming Web Application
IRAC P3 - ETSIT
This project demonstrates the development of a basic video streaming web application using the MPEG-DASH protocol. The project is divided into several parts, each focusing on different aspects of video streaming, encoding, and DRM management.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Part 1: DASH.js Introduction](#part-1-dashjs-introduction)
4. [Part 2: Video Preparation and Metrics](#part-2-video-preparation-and-metrics)
5. [Part 3: DRM Management](#part-3-drm-management)
6. [Part 4: Advanced Metrics Visualization](#part-4-advanced-metrics-visualization)
7. [Optional Part 5: Advanced DRM Management](#optional-part-5-advanced-drm-management)

## Introduction
This project involves creating a server-client web application for video streaming using the DASH.js library. The development is done within a Docker container, which provides all the necessary tools and frameworks.


## Part 1: DASH.js Introduction
- **Objective:** Deploy and use the DASH.js tool to provide a basic video streaming service.
- **Tasks:**
  - Create an `index.html` file to integrate DASH.js and stream a video using the provided MPD URL.
  - Analyze the MPD document structure (XML, MPD, Period, AdaptationSet, SegmentTemplate, Representation).

## Part 2: Video Preparation and Metrics
- **Objective:** Generate different video qualities for streaming and visualize metrics.
- **Tasks:**
  - Use `x264` to encode video into different qualities (low, medium, high).
  - Use `MP4Box` to convert encoded videos to MP4.
  - Use Bento4 to segment videos for DASH and generate an MPD file.
  - Update `index.html` to display the video and metrics (bitrate, buffer, representation).

## Part 3: DRM Management
- **Objective:** Implement DRM protection for the video content.
- **Tasks:**
  - Fragment and encrypt video files using Bento4 tools.
  - Update `index.html` to include DRM protection data.
  - Test the implementation by altering DRM keys and observing behavior.

## Part 4: Advanced Metrics Visualization
- **Objective:** Enhance the web client to display advanced metrics in real-time.
- **Tasks:**
  - Integrate JavaScript libraries like ChartJS or VisJS to visualize metrics.
  - Implement the web client to show video quality changes and buffer levels graphically.

## Optional Part 5: Advanced DRM Management
- **Objective:** Explore advanced DRM techniques and dynamic key management.
- **Tasks:**
  - Implement alternative encryption methods (e.g., Widevine, PlayReady).
  - Set up a REST API for dynamic DRM key exchange.
  - Document the implementation with detailed explanations and screenshots.

![image](https://github.com/ivalenzuelan/IracP3/assets/125378917/8ea6d556-55a9-459e-b41b-7d03e210e4f3)
