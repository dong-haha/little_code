package xyz.hzau.controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;


public class SocketTest {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("*.*.*.*", 19999);
            //Socket socket = new Socket("localhost", 19999);
            System.out.println("Client start!");
            PrintWriter out = new PrintWriter(socket.getOutputStream()); // 输出，to 服务器 socket
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream())); // 输入， from 服务器 socket
            out.println("../example3_plant.png");
            out.flush(); // 刷缓冲输出，to 服务器
            System.out.println(in.readLine()); // 打印服务器发过来的字符串
            System.out.println("Client end!");
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}

