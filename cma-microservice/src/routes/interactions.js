var express = require('express');
var router = express.Router();
const Interaction = require('../models/interactionModel');
const CommentInteraction = require('../models/commentInteractionModel')

// handling logging when a user views a piece of content
router.post('/interactions/view', async (req, res) => {
  const { userId, contentId} = req.body;

  try {
    const interaction = new Interaction({
      userId,
      contentId,
      timestamp: Date.now(),
      interactionType: 'view' 
    });
    await interaction.save();
    return res.json({ message: 'View interaction logged successfully' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// handling logging when a user likes a piece of content
router.post('/interactions/like', async (req, res) => {
  const { userId, contentId} = req.body;

  try {
    const interaction = new Interaction({
      userId,
      contentId,
      timestamp: Date.now(),
      interactionType: 'like'
    });
    await interaction.save();
    return res.json({ message: 'Like interaction logged successfully' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// handling logging when a user comments on a piece of content
router.post('/interactions/comment', async (req, res) => {
  const { userId, contentId, comment} = req.body;

  try {
    const interaction = new CommentInteraction({
      userId,
      contentId,
      comment,
      timestamp: Date.now(),
      interactionType: 'comment'
    });
    await interaction.save();
    return res.json({ message: 'Comment interaction logged successfully' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// handling logging when a user likes a piece of content
router.post('/interactions/add-to-favorites', async (req, res) => {
  const { userId, contentId } = req.body;

  try {
    const interaction = new Interaction({
      userId,
      contentId,
      timestamp: Date.now(),
      interactionType: 'add-to-favorites'
    });
    await interaction.save();
    return res.json({ message: 'Add-to-favorites interaction logged successfully' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});


module.exports = router;

