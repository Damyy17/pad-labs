from flask import Flask, jsonify
from transaction_coordinator import TransactionCoordinator
from database_participant import DatabaseParticipant

app = Flask(__name__)

coordinator = TransactionCoordinator()

db_participant1 = DatabaseParticipant(
    database_url='mongodb+srv://PADdb:UkdsWkNPdGpZ@paddb.uegzzu5.mongodb.net/cma_db?retryWrites=true&w=majority',
    database_name='cma_db',
    collection_name='test'
)

db_participant2 = DatabaseParticipant(
    database_url='mongodb+srv://PADdb:UkdsWkNPdGpZ@paddb.uegzzu5.mongodb.net/cr_db?retryWrites=true&w=majority',
    database_name='cr_db',
    collection_name='test'
)

coordinator.add_participant(db_participant1)
coordinator.add_participant(db_participant2)

@app.route('/transaction', methods=['POST'])
def start_transaction():
    try:
        # prepare phase
        decision = coordinator.prepare()

        if decision == 'COMMIT':
            # commit phase
            coordinator.commit()
            return jsonify({'message': 'Transaction committed successfully'}), 200
        else:
            # abort phase
            coordinator.abort()
            return jsonify({'message': 'Transaction aborted'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=6060, host="0.0.0.0")
