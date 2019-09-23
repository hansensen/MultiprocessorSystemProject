function suffixArray = determineSuffixArray( stringTarget )
%DETERMINESUFFIXARRAY 
% create stringMatrix
stringTarget = strcat(stringTarget,'$');
     maxRowSize = length(stringTarget)-1; % number of entries
     stringMatrix = cell(maxRowSize,1); % pre-allocation
for i = 1:length(stringTarget)-1
    currentLengthToInsert = length(stringTarget);
    stringMatrix{i} = stringTarget (i:length(stringTarget));
end
%{
stringTarget = 'xabxa';
% suffice array
stringMatrix = { ...
'xabxa$', ...
'abxa$', ...
'bxa$', ...
'xa$', ...
'a$', ...
};
%}
storeSortedStringMatrix = sort(stringMatrix); 
% contains the re-ordered indices
for i=1:length(stringMatrix)    % scan through storeSortedStringMatrix
   for j=1:length(stringMatrix) % scan through stringMatrix
       if (length(storeSortedStringMatrix{i}) == length(char(stringMatrix(j)))) % ensure equal length 1st
           lengthOfBoth = length(storeSortedStringMatrix{i});
            if strncmp(storeSortedStringMatrix{i}, stringMatrix(j), lengthOfBoth)
                suffixArray (i) = j; % store the position
            end
       end
   end
end
end