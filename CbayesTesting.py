% 对于0-9共10个数字
for A1=1:10
    % 每个数字有多少个样本
    len = length(img_list{A1,1});
    % 确定样本训练（学习）样本数目
    for A2=1:min(len,train_num)
        img_name = img_list{A1,1}(A2).name;
        im = imread([prefix,img_name]);
%         figure;imshow(im);
        % 例如：拆分成7*7=49个小块(Piece)，每个小块有4*4=16个元素
        Piece = 1;
        for A3=1:lPiece:29-lPiece
            for A4=1:lPiece:29-lPiece
                temp = im(A3:A3+lPiece-1,A4:A4+lPiece-1);
                % 例如：只要16个中有超过3个是白色,就标记为1(255*4=1020)
                if sum(sum(temp))>= 255*nthres
                    Pattern(A1).feature(Piece,A2) = 1;
                end
                Piece = Piece+1;
            end
        end
    end
    fprintf('Calss %1d:%5d images are written to mat.\n',A1-1,train_num);
end