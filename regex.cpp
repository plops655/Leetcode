#include <cstddef>  // For size_t
#include <string>   // For std::string
#include <iostream>

using namespace std;

class Solution {
    public:

        bool isAlphabet(char c) {
            if (c != '.' && c != '*') {
                return true;
            }
            return false;
        }

        bool isStar(char c) {
            return c == '*';
        }

        bool isDot(char c) {
            return c == '.';
        }

        size_t mergeStars(string p, size_t p_pt) {

            while (p_pt < p.length() && isStar(p.at(p_pt))) {
                p_pt += 1;
            }

            return p_pt;
        }

        bool isMatch(string s, string p, size_t s_pt, size_t p_pt, char prev_char) {

            while (s_pt < s.length() && p_pt < p.length()) {
                char curr_char = p.at(p_pt);
                if (isAlphabet(curr_char)) {
                    if (s.at(s_pt) != curr_char) {
                        return false;
                    }
                    prev_char = curr_char;
                    s_pt += 1;
                    p_pt += 1;
                } else if (isStar(curr_char)) {

                    // merge stars

                    p_pt = mergeStars(p, p_pt);
                    if (isAlphabet(prev_char)) {
                        return isMatch(s, p, s_pt, p_pt + 1, prev_char) || (isMatch(s, p, s_pt + 1, p_pt, prev_char) && s.at(s_pt) == prev_char);
                    }


                    if (isDot(prev_char)) {
                        return isMatch(s, p, s_pt, p_pt + 1, prev_char) || isMatch(s, p, s_pt + 1, p_pt, prev_char);
                    }
                } else if (isDot(curr_char)) {
                    prev_char = curr_char;
                    s_pt += 1;
                    p_pt += 1;
                }
            }

            if (s_pt >= s.length() && p_pt >= p.length()) {
                return true;
            }

            return false;       
        }
        
        bool isMatch(string s, string p) {
            return isMatch(s, p, 0, 0, '\0');
        }
};


int main() {

    Solution solution;
    string s = "ab";
    string p = ".*";

    bool is_match = solution.isMatch(s, p);
    cout << "result: " << is_match << endl;

}