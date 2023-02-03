class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> &image)
    {
        for (int i = 0; i < image.size(); i++)
        {
            int start = 0;
            if (image[i].size() == 1)
            {
                image[i][start] = !(image[i][start]);
                continue;
            }
            for (int j = image[i].size() - 1; j >= image[i].size() / 2; j--)
            {
                int temp = !(image[i][start]);
                image[i][start] = !(image[i][j]);
                image[i][j] = temp;
                start++;
            }
        }
        return image;
    }
};