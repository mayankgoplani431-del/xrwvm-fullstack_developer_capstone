# Cars Dealership - Full Stack Developer Capstone

Cars Dealership is a full-stack web application for a national car retailer in the U.S.
Users can browse dealership branches, filter them by state, read reviews with sentiment analysis,
and post their own reviews after logging in.

## Architecture
- **Django** (`server/djangoproj`, `server/djangoapp`): user login, logout and registration, car makes and models, proxy to the other services.
- **React** (`server/frontend`): dealers list, dealer details, post review, login and sign-up pages.
- **Node.js / Express / MongoDB** (`server/database`): dealerships and reviews API.
- **Flask** (`server/djangoapp/microservices`): sentiment analyzer for review text.
