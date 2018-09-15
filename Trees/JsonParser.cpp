#include <iostream>
#include <vector>
#include <string>
#include <list>
//SPLIT and others
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
//Lower Case types algo
#include <algorithm>
//StringStream
#include <sstream>

using namespace std;
using namespace boost;

struct GenericJsonNode {
	GenericJsonNode() {
	}

	virtual ~GenericJsonNode()=0;
	virtual vector<GenericJsonNode*> getChildren()=0;
};

struct StringJsonNode : public GenericJsonNode {
	
	StringJsonNode(string key) {
		this->key = key;
	}

	~StringJsonNode() {

	}

	vector<GenericJsonNode*> getChildren() {
		return children;
	}

	string key;
	vector<GenericJsonNode*> children;
};

struct DoubleJsonNode : public GenericJsonNode {
	
	DoubleJsonNode(double key) {
		this->key = key;
	}

	~DoubleJsonNode() {

	}

	vector<GenericJsonNode*> getChildren() {
		return children;
	}

	double key;
	vector<GenericJsonNode*> children;
};

struct BooleanJsonNode : public GenericJsonNode {
	
	BooleanJsonNode(bool key) {
		this->key = key;
	}

	~BooleanJsonNode() {

	}

	vector<GenericJsonNode*> getChildren() {
		return children;
	}

	bool key;
	vector<GenericJsonNode*> children;
};

class JsonParser {
	
public:
	typedef enum {

		NUMERIC_TYPE=1,
		STRING_TYPE,
		BOOL_TYPE,
		INVALID_TYPE

	} valueType;

	JsonParser() : _root(NULL){

	}

	template<typename TYPE>
	void buildJsonTree(list<string> keys, TYPE value) {

		_root = new StringJsonNode(keys.front());

		keys.pop_front();

		for(auto key : keys) {
			GenericJsonNode* node = new StringJsonNode(key);
			_root->getChildren().push_back(node);
		}

//		_root->getChildren()[_root->getChildren().size()-1]->getChildren().push_back(new StringJsonNode(value));
	}
	
	template<typename TYPE>
	void displayJsonTree(GenericJsonNode* root) {

	}
		
	valueType extractInfo(string text, list<string>& keys, string& stringValue , double& doubleValue, bool& booleanValue) 
	{
		std::size_t found = text.find_first_of("=");
	
		string key = "";
		string value = "";

		//Processing Key, Value
		if(found != std::string::npos) {
	
			key = text.substr(0,found);
	
			//Processing Keys
			split(keys, key, boost::is_any_of("."));
	
			value = text.substr(found+1,text.length());

			//iValue = value;
	
			if(!value.empty()) {
				//Case1: Checking if value is in ""
				if(value[0] == '"' && value[value.length()-1] == '"') {
					cout << "string value is : " << value << endl;
					stringValue += value;
					return valueType::STRING_TYPE;
				}
	
				//Case2: If the input string is not correct
				else if(value[0] == '"' || value[value.length()-1] == '"') {
					cout << "Invalid string Input!!" << endl;
					return valueType::INVALID_TYPE;
				}
				else {
					string value1 = value;
					transform(value1.begin(),value1.end(),value1.begin(),::tolower);
	
					//Case3:boolean case	
					if(value1 == "true" || value1 == "false") {
	
						istringstream is(value1);
	
						is >> std::boolalpha >> booleanValue;
	
						cout << "Value is boolean : " << booleanValue << endl;
					}
					else {
						try {
							//Case4: Numeric
	
							double number = boost::lexical_cast<double>(value);
	
							cout << "Input value is Numeric!!" << endl;
	
							cout << "Number is : " << number << endl;
	
							return valueType::NUMERIC_TYPE;
						}
						catch(boost::bad_lexical_cast& ) {
							//Case5: String not in quotes
	
							cout << "String is not in quotes, invalid input!!" << endl;
	
							return valueType::INVALID_TYPE;
						}
					}
	
				}
			}
			else {
				cout << "value is null" << endl;
				value = "NULL";
				return valueType::STRING_TYPE;
			}
		}
		else {
			cout<<"Incorrect Input!!" << endl;
			return valueType::INVALID_TYPE;
		}
	}	

private:
	GenericJsonNode* _root;
};

int main() {

	JsonParser* jp =  new JsonParser();
	
	string text = "a.b.c=\"123\"";
	string text1 = "a.b.c=123";
	string text2 = "a.b.c=TRUE";
	string text3 = "a.b.c=a123b";
	string text4 = "a.b.c=\"a123b";
	string text5 = "a.b.c=\"http://stackoverflow.com/questions/3613284/c-stdstring-to-boolean\"";
	string text6 = "a.b.c=123.12";
	string text7 = "a.b.c";
	string text8 = "a.b.c=";
	
	list<string> keys;
	//auto value;
	std::string stringValue = "";
	double doubleValue = 0 ;
	bool boolValue;
	
	int valueType = jp->extractInfo(text, keys, stringValue, doubleValue, boolValue);
	
	if( valueType == jp->valueType::STRING_TYPE) {
		cout << "Value is of STRING type" << endl;
		//jp->buildJsonTree<string>(keys,stringValue);
	} 
	else if (valueType == jp->valueType::NUMERIC_TYPE) {
		cout << "Value is of NUMERIC type" << endl;
		jp->buildJsonTree<double>(keys,doubleValue);
	}
	else if (valueType == jp->valueType::BOOL_TYPE) {
		cout << "Value is of BOOLEAN type" << endl;
		jp->buildJsonTree<bool>(keys,boolValue);
	}
	else if (valueType == jp->valueType::INVALID_TYPE) {
		cout << "Value is INVALID" << endl;	
	}

	return 0;
}
