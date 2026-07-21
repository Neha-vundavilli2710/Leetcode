class Solution {

    public String longestCommonPrefix(String[] strs) {

        if (strs == null || strs.length == 0) {
            return "";
        }

        String s = strs[0];

        for (int i = 1; i < strs.length; i++) {

            while (!strs[i].startsWith(s)) {

                s = s.substring(0, s.length() - 1);

                if (s.length() == 0) {
                    return "";
                }
            }
        }

        return s;
    }
}