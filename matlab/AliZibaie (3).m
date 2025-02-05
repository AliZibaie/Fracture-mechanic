theta = linspace(0, 2*pi, 100);  
d = 0.005; 

KI = 28;
ay = 300;
v = 0.34;

r1 = (0.5+0.5*cos(theta)+1.5.*(sin(theta).^2)).*(1/(2*pi)*(KI/ay)^2);  
r2 = (((1-v^2)/2)*(1+cos(theta))+(3/4).*(sin(theta).^2))*(1/(2*pi)*(KI/ay)^2);  

x1 = r1 .* cos(theta);
y1 = zeros(size(theta));
z1 = r1 .* sin(theta); 
x2 = r2 .* cos(theta);
y2 = d * ones(size(theta));
z2 = r2 .* sin(theta); 
x3 = r2 .* cos(theta);
y3 = 4*d * ones(size(theta));
z3 = r2 .* sin(theta); 
x4 = r1 .* cos(theta);
y4 = 5*d * ones(size(theta));
z4 = r1 .* sin(theta);

figure;
hold on;
plot3(x1, y1, z1, 'b', 'LineWidth', 2);  
plot3(x2, y2, z2, 'r', 'LineWidth', 2);  
plot3(x3, y3, z3, 'r', 'LineWidth', 2);
plot3(x4, y4, z4, 'b', 'LineWidth', 2);

connections = {x1, x2, x3, x4};  
connections_y = {y1, y2, y3, y4};  
connections_z = {z1, z2, z3, z4}; 

for i = 1:length(theta)
    for j = 1:3  
        plot3([connections{j}(i) connections{j+1}(i)], ...
              [connections_y{j}(i) connections_y{j+1}(i)], ...
              [connections_z{j}(i) connections_z{j+1}(i)], 'k'); 
    end
end

axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
grid on;
title('');
hold off;