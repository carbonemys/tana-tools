# Flask-based Web API

This repository contains a Flask-based web application designed to provide an interface to extract transcripts and details from various web content sources like YouTube videos, PDF documents, and Tweets.

## Features

- Serve HTML pages
- Extract transcript from YouTube videos
- Extract details from YouTube videos
- Extract transcript from PDF documents
- Extract information from tweets (username and content)

## Endpoints

The service exposes several HTTP GET endpoints:

- `/youtube_transcript` - returns a transcript of a YouTube video, with a newline after every sentence if requested.
- `/youtube_detail` - returns specific details about a YouTube video.
- `/pdf_transcript` - returns a transcript from a provided PDF document URL.
- `/tweet` - returns specific details about a tweet.
- `/mermaid_graph` with `?encoded_graph=` returns a url for a mermaid graph

## Usage

To use these endpoints, provide the necessary arguments as URL parameters. Below is an example for each endpoint:

1. `http://localhost:8080/youtube_transcript?youtube_url=<YouTube-Video-URL>&newline=true` - serves transcript from the YouTube video.
2. `http://localhost:8080/youtube_detail?youtube_url=<YouTube-Video-URL>&youtube_detail=<Detail-Name>` - serves specified detail about the YouTube video.
3. `http://localhost:8080/pdf_transcript?pdf_url=<PDF-URL>` - serves transcript of the provided PDF document.
4. `http://localhost:8080/tweet?tweet_url=<Tweet-URL>&twitter_detail=<Detail-Name>` - serves specified detail from the Tweet. (`twitter_detail` is optional, defaults to content)
