#pragma once

#include "HttpResponse.hpp"
#include "Server.hpp"

/*
 * Client class handles
 * requests and responses
 **/
class Client : public Fd {
   public:
    Client(Server& server);
    ~Client();

    void handlePollin(int index);
    void handlePollout(int index);

   private:
    Server& _server;
    HttpRequest _request;
    HttpResponse _response;

    std::string _path;

    int parseRequest(const std::string& uri);

    void error(int statusCode);
};
