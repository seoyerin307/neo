const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = 3000;

// 정적 파일 경로 설정
app.use(express.static(path.join(__dirname, 'public')));

const NEWS_API_KEY = 'YOUR_NEWS_API_KEY';
const NEWS_API_URL = 'https://newsapi.org/v2/top-headlines';

app.get('/api/news', async (req, res) => {
  try {
    const response = await axios.get(NEWS_API_URL, {
      params: {
        country: 'kr',
        category: 'general',
        apiKey: NEWS_API_KEY
      }
    });

    const articles = response.data.articles;

    // 간단 요약 + 조회수 없으므로 시간 기준 정렬
    const sorted = articles
      .sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt))
      .map((a, i) => ({
        id: i,
        title: a.title,
        summary: a.description || '요약 없음',
        url: a.url,
        image: a.urlToImage,
        publishedAt: a.publishedAt,
        audioUrl: `https://dummy.com/audio${i}.mp3` // 실제 TTS 파일로 대체 예정
      }));

  res.json(sorted);
  } catch (error) {
    console.error('뉴스 API 오류:', error.message);
    res.status(500).json({ error: '뉴스를 가져오지 못했습니다.' });
  }
});

app.listen(PORT, () => {
  console.log(`서버 실행 중: http://localhost:${PORT}`);
});