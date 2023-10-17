var express = require('express');
var router = express.Router();
const Interaction = require('../models/interactionModel');

// handling logging when a user views a piece of content
router.post('/interactions/view', async (req, res) => {
  const { userId, contentId, timestamp } = req.body;

  try {
    const interaction = new Interaction({
      userId,
      contentId,
      timestamp,
      type: 'view' 
    });
    await interaction.save();
    return res.json({ message: 'View interaction logged successfully' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/interactions/like', async (req, res) => {
  const { userId, contentId, timestamp } = req.body;

  const interaction = new Interaction({
    userId,
    contentId,
    timestamp,
    type: 'like'
  });

  await interaction.save((err) => {
    if (err) {
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    return res.json({ message: 'Like interaction logged successfully' });
  });
});

router.post('/interactions/comment', async (req, res) => {
  const { userId, contentId, comment, timestamp } = req.body;

  const interaction = new Interaction({
    userId,
    contentId,
    comment,
    timestamp,
    type: 'comment'
  });

  await interaction.save((err) => {
    if (err) {
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    return res.json({ message: 'Comment interaction logged successfully' });
  });
});

router.post('/interactions/add-to-playlist', async (req, res) => {
  const { userId, contentId, playlistId, timestamp } = req.body;

  const interaction = new Interaction({
    userId,
    contentId,
    playlistId,
    timestamp,
    type: 'add-to-playlist'
  });

  await interaction.save((err) => {
    if (err) {
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    return res.json({ message: 'Add-to-playlist interaction logged successfully' });
  });
});


module.exports = router;

