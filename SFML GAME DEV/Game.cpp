#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <iostream>

class Game {

public:
    Game();
    void run();

private:
    void processEvents();
    void handlePlayerInput(sf::Keyboard::Key, bool);
    void update(sf::Time);
    void render();

private:
    sf::RenderWindow mWindow;
    sf::CircleShape mPlayer;
    bool mIsMovingUp;
    bool mIsMovingDown;
    bool mIsMovingRight;
    bool mIsMovingLeft;
    float PlayerSpeed;
};

Game::Game()
    : mWindow(sf::VideoMode({ 640, 480 }), "SFML 3.0.2 Application"),
    mPlayer(40.f),
    mIsMovingUp(false),
    mIsMovingDown(false),
    mIsMovingRight(false),
    mIsMovingLeft(false),
    PlayerSpeed(200.f)
{
    std::cout << "Hi Aaron, Welcome" << std::endl;
    mPlayer.setPosition({ 100.f, 100.f });
    mPlayer.setFillColor(sf::Color::Cyan);
}

void Game::run() {
    const sf::Time TIMEPERFRAME = sf::seconds(1.f / 60.f);
    sf::Clock clock;
    sf::Time timeSinceLastUpdate = sf::Time::Zero;
    
    while (mWindow.isOpen())
    {
        processEvents();
        timeSinceLastUpdate += clock.restart();

        while (timeSinceLastUpdate > TIMEPERFRAME)
        {
            timeSinceLastUpdate -= TIMEPERFRAME;
            processEvents();
            update(TIMEPERFRAME);
        }
        render();
    }
}

void Game::processEvents() {
    while (auto event = mWindow.pollEvent()) {
        if (event->is<sf::Event::Closed>()) {
            mWindow.close();
        }
        else if (const auto* keyPressed = event->getIf<sf::Event::KeyPressed>()) {
            handlePlayerInput(keyPressed->code, true);
        }
        else if (const auto* keyReleased = event->getIf<sf::Event::KeyReleased>()) {
            handlePlayerInput(keyReleased->code, false);
        }
    }
}

void Game::handlePlayerInput(sf::Keyboard::Key key, bool isPressed) {
    if (key == sf::Keyboard::Key::W)
        mIsMovingUp = isPressed;
    else if (key == sf::Keyboard::Key::S)
        mIsMovingDown = isPressed;
    else if (key == sf::Keyboard::Key::A)
        mIsMovingLeft = isPressed;
    else if (key == sf::Keyboard::Key::D)
        mIsMovingRight = isPressed;
}

void Game::update(sf::Time deltaTime) {
    sf::Vector2f movement(0.f, 0.f);
    if (mIsMovingUp) movement.y -= PlayerSpeed;
    if (mIsMovingDown) movement.y += PlayerSpeed;
    if (mIsMovingLeft) movement.x -= PlayerSpeed;
    if (mIsMovingRight) movement.x += PlayerSpeed;

    mPlayer.move(movement * deltaTime.asSeconds());
}

void Game::render() {
    mWindow.clear();
    mWindow.draw(mPlayer);
    mWindow.display();
}

int main() {
    Game game;
    game.run();
}
