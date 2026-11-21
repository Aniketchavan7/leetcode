// SQL:
// SELECT tweet_id 
// FROM Tweets 
// WHERE CHAR_LENGTH(content) > 15;

class Solution {
    public List<Integer> invalidTweets(int[] tweetIds, String[] contents) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < tweetIds.length; i++) {
            if (contents[i].length() > 15) {
                res.add(tweetIds[i]);
            }
        }
        return res;
    }
}
