FROM atendai/evolution-api:v1.8.2

EXPOSE ${PORT}

CMD ["npm", "start"] 