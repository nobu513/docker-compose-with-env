FROM rust:1.63

RUN cargo new --bin app 
WORKDIR /app

COPY Cargo.toml .
RUN cargo install --path .

RUN rm ./src/*.rs

COPY ./src ./src

CMD ["cargo", "run"]