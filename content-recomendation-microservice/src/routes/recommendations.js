const express = require('express');
const router = express.Router();
const axios = require('axios');
const Recommendation = require('../model/recommendationModel');
const Content = require('../model/contentModel');

// Endpoint to get content from recommendations for a user
router.get('/recommendations/:userId/:contentId', async (req, res) => {
  const { userId, contentId } = req.params;

  try {
    const content = await Content.findOne({ contentId });
    if (content) {
      const recommendation = await Recommendation.findOne({
        $and: [
          {userId},
          {recommendations: {$in: contentId}}
        ]
      });
      if (recommendation) {
        res.json(content);
      } else {
        res.status(404).json({ error: 'Recommendation not found' });
      }
    } else {
      res.status(404).json({ error: 'Content not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.get('/recommendations/:userId', async (req, res) => {
  const { userId } = req.params;

  try {
    const interactionsResponse = await axios.get(`http://localhost:3000/receive-interactions/${userId}`);
    const contentIds = interactionsResponse.data.contentIds;
    console.log(`ContentIds from cma service - ${contentIds}`);

    const contentRecommendations = [];
    console.log("Generating of content \n");
    for (const contentId of contentIds) {
      // finding the content by contentId to get its genre
      const content = await Content.findOne({contentId});
      // console.log(content);
      if (content) {
        const genre = content.genre;
        console.log(genre);
        // fetching related content by genre
        const relatedContents = await Content.find({ genre: {$in: genre} });
        // console.log(relatedContents);
        // generating recommendations based on same genres
        contentRecommendations.push(...relatedContents
          .filter(relatedContent => relatedContent.contentId !== contentId) // exclude the original content
          .map(relatedContent => relatedContent.contentId));
          
        console.log(contentRecommendations);
      }
    }

    // saving generetated recommendations to database
    const recommendationModel = new Recommendation({
      recommendationId: Date.now() + Math.floor(Math.random() * 1000), 
      userId: userId,
      recommendations: contentRecommendations
    });
    console.log(recommendationModel);
    await recommendationModel.save();

    res.json(recommendationModel);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

module.exports = router;