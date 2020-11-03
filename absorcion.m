%% Constantes
global anchoP anchoG anchoM anchoH;
anchoP=1; %radio piel
anchoG=2; %radio grasa
anchoM=3; %radio músculo
anchoH=4; %radio hueso
r=(anchoP+anchoG+anchoM+anchoH);
z=10;  %largo del brazo cm

muP=0.23456;     %Coeficiente de atenuacion lineal total hueso cm
muP_foto=0.1789; %Coeficiente de atenuacion lineal absorcion hueso cm
muG=0.9876;      %Coeficiente de atenuacion lineal total grasa cm
muG_foto=0.4321; %Coeficiente de atenuacion lineal absorcion grasa cm
muM=1.234;       %Coeficiente de atenuacion lineal total músculo cm
muM_foto=0.5678; %Coeficiente de atenuacion lineal absorcion músculo cm
muH=2.3456;      %Coeficiente de atenuacion lineal total piel cm
muH_foto=0.2345; %Coeficiente de atenuacion lineal absorcion piel cm
mu=[muP, muP_foto,muG, muG_foto,muM, muM_foto,muH, muH_foto,muM, muM_foto,muG, muG_foto,muP, muP_foto];
fotones=2000;    % número de fotones

%% Fotones

foton=zeros(fotones,3);
foton(:, 3)=pi*rand(fotones,1)+pi/2;
foton(:, 2)=r.*sin(foton(:, 3));
foton(:, 1)=r.*cos(foton(:, 3));
foton(:, 3)=z*rand(fotones,1);
%plot(foton(:,1),foton(:,2), 'o', 'MarkerSize', 5)
%% Montecarlo
nu=zeros(fotones,4);
nu(:,1)=-log(rand(fotones,1))/muP; %distancia aleatoria que va a atravesar el fotón en piel
nu(:,2)=-log(rand(fotones,1))/muG; %distancia aleatoria que va a atravesar el fotón en grasa
nu(:,3)=-log(rand(fotones,1))/muM; %distancia aleatoria que va a atravesar el fotón en músculo
nu(:,4)=-log(rand(fotones,1))/muH; %%distancia aleatoria que va a atravesar el fotón en hueso
nu(:,5)=-log(rand(fotones,1))/muM; %musculo
nu(:,6)=-log(rand(fotones,1))/muG; %grasa
nu(:,7)=-log(rand(fotones,1))/muP; %piel
%%
foton_abs=0;
foton_int=0;
fid=fopen('datos.txt','w');
fclose(fid);
for r = 1:fotones
dist_x=distancias(foton(r,:));
a=nu(r, :)<dist_x;
fid=fopen('datos.txt','a+');
if sum(a)>0
    foton_int=foton_int+1;
    s=find(a,1,'first');
    if rand<mu(2*s)/mu(2*s-1)
        foton_abs=foton_abs+1;
    else
        compton=foton(r,:);
        compton(1)=compton(1)+nu(r,s);
        for u=1:s-1
        compton(1)=compton(1)+dist_x(u);
        end
        %fprintf('%f %f %f\n', [compton(1), compton(2), compton(3)]);
        fprintf(fid, '%f %f %f\n',[compton(1), compton(2), compton(3)]);
    end
end
end
fclose(fid);
fprintf('\n Se absorbieron: %i fotones. Interactuaron %i fotones. %i', foton_abs, foton_int);