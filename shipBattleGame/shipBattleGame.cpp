#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>
using namespace std;

class ShipBattle {
public:
	ShipBattle(int shipNumber) {
		_shipNumber = shipNumber;	
	}
	
	void setEnemyBattleMap(vector<int>& battleMap) {
		_battleMap = battleMap;
	}

	bool destroyEnemyShip(int location) {
		return _battleMap[location];
	}

	int getMyShips() {
		return _shipNumber;
	}

private:
	vector<int> _battleMap;
	int _shipNumber;
	
};

int main() {

	ShipBattle* player1 = new ShipBattle(4);

	ShipBattle* player2 = new ShipBattle(4);

	vector<int> player1Map = {0,0,0,1,0,1,1,0,1};
	vector<int> player2Map = {1,0,0,1,1,0,1,0,0};

	player1->setEnemyBattleMap(player2Map);
	player2->setEnemyBattleMap(player1Map);

	int player1Ships = 4;

	int player2Ships = 4;

	while(true) {

		if(player1Ships == 0  && player2Ships > 0) {
			cout << "Player1 says: though i am destroyed but i will rise again for the ashes" << endl;
			break;
		}

		if(player1Ships > 0  && player2Ships == 0) {
			cout << "Player2 says: I am defeted, this is not possible, thou shall burn in hell!!!" << endl;
			break;
		}
		if(player1Ships == 0  && player2Ships ==  0) {
			cout << "Player1 says: we are equal" << endl;
			cout << "Player2 says: you showed talent boy.." << endl;
			break;
		}

		srand(time(NULL));
		if(player1->destroyEnemyShip(rand()%10)) {
			--player2Ships;
		}

		srand(time(NULL)+1);
		if(player2->destroyEnemyShip(rand()%10)) {
			--player1Ships;
		}
	}
	return 0;
}
