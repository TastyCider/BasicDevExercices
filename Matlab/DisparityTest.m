

%%
% Load the stereo images.
left = imread('left.png');
right = imread('right.png');
frameLeftGray  = mean(left,3);
frameRightGray = mean(right,3);

Blocksize=15;
mask = ones(Blocksize);
Lin=size(frameLeftGray,1);
Col=size(frameLeftGray,2);
DispMap=zeros(Lin,Col,'single');
SearchRange=50;

for l=1:Lin
    a= max(l-(Blocksize-1)/2,1);
    b=min (l+(Blocksize-1)/2,Lin);
    for k =1:Col
            c= max(k-(Blocksize-1)/2,1);
            d= min (k+(Blocksize-1)/2,Col);
        W=frameRightGray([a:b],[c:d]);
        maxS= min(SearchRange,Col-d);
        minS= 0; %max(-SearchRange,1-c);
        SADvec=zeros(1,maxS-minS+1);
        for m= minS:maxS
            SADvec(m - minS+1)= sum(sum(abs(W-frameLeftGray([a:b],(c+m):(d+m)))));
        end
     [e,f]=min(SADvec,[],2);
     DispMap(l,k)=f+minS-1;
    end
end
%%
image(DispMap)
colormap('jet');
colorbar;

