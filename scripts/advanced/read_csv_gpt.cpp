// csv_reader.cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstring>

using namespace std;

struct CSVRow {
    char date[20];
    float floatValue;
};

vector<CSVRow> readCSV(const string& filePath, unsigned& intValue) {
    vector<CSVRow> data;
    ifstream file(filePath);

    if (!file.is_open()) {
        cerr << "Error opening file: " << filePath << endl;
        return data;
    }

    string line;
    string stringValue;
    getline(file, line);
    istringstream iss(line);
    string stringVal, intStr;
    if (getline(iss, stringVal, ',') && getline(iss, intStr, ',')) {
        stringValue = stringVal;
        // Convert the string to an unsigned integer
        intValue = (intStr.empty()) ? 0 : stoi(intStr);
    }

    while (getline(file, line)) {
        istringstream iss(line);
        string dateStr, floatStr;

        if (getline(iss, dateStr, ',')) {
            getline(iss, floatStr, ',');
            CSVRow row;
            strncpy(row.date, dateStr.c_str(), sizeof(row.date));
            row.date[sizeof(row.date) - 1] = '\0'; // Ensure null termination

            // Convert the float string to a float value
            row.floatValue = (floatStr.empty()) ? -9999.0f : stof(floatStr);

            data.push_back(row);
        }
    }

    file.close();
    return data;
}

extern "C" CSVRow* processCSVFile(const char* filePath, unsigned* total, size_t* size) {
    vector<CSVRow> csvData = readCSV(filePath, *total);
    *size = csvData.size();

    // Allocate memory for CSVRow array
    CSVRow* result = new CSVRow[csvData.size()];

    // Copy data to the allocated array
    std::copy(csvData.begin(), csvData.end(), result);

    return result;
}

extern "C" void freeCSVRows(CSVRow* rows) {
    // Free the allocated memory
    delete[] rows;
}

// **************************************************
// Fast version 
// **************************************************


vector<CSVRow> readCSVFast(const string& filePath, unsigned& intValue) {
    vector<CSVRow> data;
    ifstream file(filePath);

    if (!file.is_open()) {
        cerr << "Error opening file: " << filePath << endl;
        return data;
    }

    string line;
    string stringValue;
    getline(file, line);
    istringstream iss(line);
    string stringVal, intStr;
    if (getline(iss, stringVal, ',') && getline(iss, intStr, ',')) {
        stringValue = stringVal;
        // Convert the string to an unsigned integer
        intValue = (intStr.empty()) ? 0 : stoi(intStr);
    }

    while (getline(file, line)) {
        istringstream iss(line);
        string dateStr, floatStr;

        if (getline(iss, dateStr, ',')) {
            getline(iss, floatStr, ',');
            CSVRow row;
            strncpy(row.date, dateStr.c_str(), sizeof(row.date));
            row.date[sizeof(row.date) - 1] = '\0'; // Ensure null termination

            // Convert the float string to a float value
            row.floatValue = (floatStr.empty()) ? -9999.0f : stof(floatStr);

            data.push_back(row);
        }
    }

    file.close();
    return data;
}

extern "C" void* processCSVFileFast(const char* filePath, unsigned* total, size_t* size, size_t* rowSize) {
    vector<CSVRow> csvData = readCSVFast(filePath, *total);
    *size = csvData.size();
    *rowSize = sizeof(CSVRow);

    // Allocate memory for CSVRow array
    void* result = malloc(csvData.size() * sizeof(CSVRow));
    if (!result) {
        cerr << "Memory allocation failed" << endl;
        return nullptr;
    }

    // Copy data to the allocated array
    memcpy(result, csvData.data(), csvData.size() * sizeof(CSVRow));

    return result;
}

extern "C" void freeCSVRowsFast(void* rows) {
    // Free the allocated memory
    free(rows);
}