const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const interactionSchema = new Schema({
  userId: String,
  contentId: String,
  interactionType: String,
  timestamp: Date,
});

const Interaction = mongoose.model('Interaction', interactionSchema);

module.exports = Interaction;