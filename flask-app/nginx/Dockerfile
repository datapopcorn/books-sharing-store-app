# Use the Nginx image
FROM nginx
 
COPY index.html /usr/share/nginx/html/
 
# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
 
# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
 
COPY ssl.crt /etc/nginx/ssl.crt
COPY ssl.key /etc/nginx/ssl.key
 
EXPOSE 443