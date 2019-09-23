clear all; clc; 
% stringTarget = 'xabxa';
stringTarget = 'banana';
%DETERMINESUFFIXARRAY 
suffixArray = determineSuffixArray( stringTarget )

suffixArray = suffixArray - 1



%%
clear;clc;
stringTarget = 'banana apple';

%split the string in seperat blocks

blocks = 3;
m = length(stringTarget)/blocks;
b = @(n) stringTarget((n-1)*m+1:(n*m));






%stringTarget2 = [strcat(b(1),'$'), strcat(b(2),'$')]
stringMatrix = cell(m,blocks); % pre-allocation
for p = 1:blocks
    

    stringTarget2(p,:) = strcat(b(p),'$');
    maxRowSize(p) = length(b(p))-1; % number of entries
    
    for i = 1:length(b(p))
        currentLengthToInsert = length(b(p));
        stringMatrix{i,p} = stringTarget2(p,i:length(b(p)));
    end



storeSortedStringMatrix(p,:) = sort(stringMatrix(:,p)); 
% contains the re-ordered indices
for i=1:length(stringMatrix)    % scan through storeSortedStringMatrix
   for j=1:length(stringMatrix) % scan through stringMatrix
       if (length(storeSortedStringMatrix{p,i}) == length(char(stringMatrix(j)))) % ensure equal length 1st
           lengthOfBoth = length(storeSortedStringMatrix{p,i});
            if strncmp(storeSortedStringMatrix{p,i}, stringMatrix(j,p), lengthOfBoth)
                suffixArray(p,i) = j-1; % store the position
            end
       end
   end
end

end



%%




















