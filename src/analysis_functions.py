def count_stations_per_state(df):
    """
    Calculates the number of weather stations in each German state ("Bundesland").
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
    Returns:
        pd.Series: A Series showing the count of stations per state, sorted in descending order.
    """
    stations_per_state = df["Bundesland"].value_counts().sort_values(ascending=False)
    return stations_per_state

def plot_stations_per_state(state_counts):
    """
    Generates a horizontal bar plot showing the distribution of charging stations across German states.
    Args:
        state_counts (pd.Series): A Series showing the count of stations per state, sorted in descending order.
    Returns:
        None: Displays the Matplotlib plot.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x=state_counts.values, y=state_counts.index, palette="viridis")
    plt.title("Charging Stations per German State")
    plt.xlabel("Number of Stations")
    plt.ylabel("State")
    plt.show()

#Function calls
state_counts = count_stations_per_state(df)
print(state_counts)
plot_stations_per_state(state_counts)



df = pd.read_csv("ev_charging_germany.csv", sep=";", encoding="utf-8")
def summarize_station_extremes(df):
    """
    Calculates and prints the German states with the maximum and minimum number of charging stations.
    Args:
        df (pd.DataFrame): The input DataFrame containing the raw station data, which must include a column named 'Bundesland'.
    Returns:
        None: Prints the results directly to the console.
    """
    #df = pd.read_csv("ev_charging_germany.csv", sep=";", encoding="utf-8")
    stations_per_state = df["Bundesland"].value_counts().rename("count").reset_index()
    stations_per_state.columns = ["name", "count"]
    
    max_state = stations_per_state.iloc[0]
    min_state = stations_per_state.iloc[-1]
    
    print(f"State with most charging stations: {max_state['name']} ({int(max_state['count'])} stations)")
    print(f"State with least charging stations: {min_state['name']} ({int(min_state['count'])} stations)")

def show_distribution_of_charging_stations(df):
    """
    Generates a Choropleth map visualizing the geographical distribution and density of charging stations across German states ('Bundeslaender').
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
    Returns:
        None: Displays the Matplotlib Choropleth map directly to the notebook output.
    """
    
    geojson_url = "https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/master/2_bundeslaender/1_sehr_hoch.geo.json"
    bundeslaender = gpd.read_file(geojson_url)
    
    merged = bundeslaender.merge(stations_per_state, on="name", how="left")
    merged["count"] = merged["count"].fillna(0)  # filling in missing states with 0 value
    
    plt.figure(figsize=(12, 14))
    ax = merged.plot(column="count", cmap="viridis", legend=True, edgecolor="black")
    plt.title("Charging Station Density by German State", fontsize=16)
    plt.axis("off")
    plt.show()

show_distribution_of_charging_stations(df)
summarize_station_extremes(df)


def find_top_city_excluding_majors(df, excluded_cities):
    """
    Filters the DataFrame to exclude specified major German cities, then finds and prints the city with the highest number of charging stations among the remaining cities.
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
        excluded_cities (list): A list of strings representing the cities to exclude from the analysis (e.g., ["Berlin", "München"]).
    Returns:
        None: Prints the result directly to the console.
    """
    filtered_df = df[~df["Ort"].isin(excluded_cities)]

    city_counts = filtered_df["Ort"].value_counts().reset_index()
    city_counts.columns = ["city", "station_count"]

    top_city = city_counts.iloc[0].to_dict()

    exclusion_str = ", ".join(excluded_cities)

    print("City with most charging stations (excluding " + exclusion_str + "): " + top_city['city'] + " (" + str(int(top_city['station_count'])) + " stations)")


def summarize_amberg_stats(df, city_name="Amberg"):
    """
    Calculates and prints the total station count and maximum installed charging power for a specified city.
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
    Returns:
        tuple: A tuple containing (station_count, max_power_kW).
    """
    amberg_df = df[df["Ort"] == city_name]

    amberg_station_count = len(amberg_df)
    amberg_max_power = amberg_df["InstallierteLadeleistungNLL"].sum()

    print("\n" + city_name + " total stations: " + str(amberg_station_count))
    print(city_name + " total maximum charging power (kW): " + str(amberg_max_power))
    
    #return amberg_station_count, amberg_max_power


def plot_amberg_stations(df, city_name="Amberg", center_coords=[49.4478, 11.8583], zoom=13):
    """
    Generates an interactive Folium map visualizing the location of charging stations within a specified city.
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
    Returns:
        folium.Map: The generated interactive map object.
    """

    amberg_df = df[df["Ort"] == city_name]
    

    amberg_map = folium.Map(location=center_coords, zoom_start=zoom)


    for _, row in amberg_df.iterrows():
        popup_text = row['Betreiber'] + " (" + str(row['InstallierteLadeleistungNLL']) + " kW)"
        
        folium.CircleMarker(
            location=[row["Breitengrad"], row["Laengengrad"]],
            radius=5,
            popup=popup_text,
            color="blue",
            fill=True
        ).add_to(amberg_map)

    return amberg_map

excluded_cities = ["Berlin", "Hamburg", "München", "Munich", "Köln", "Cologne"]
find_top_city_excluding_majors(df, excluded_cities)
summarize_amberg_stats(df)
plot_amberg_stations(df)


def find_top_operators(df):
    """
    Prints the top 5 operators and their total number of charginf points throughout Germany
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
        
    Returns:
        None: Prints the result directly to the console.
    """
    top_operators = (
        df.groupby("Betreiber")["AnzahlLadepunkteNLL"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    
    
    print("Top 5 Charging Station Operators in Germany:")
    for i, (operator, points) in enumerate(top_operators.items(), 1):
        print(f"{i}. {operator}: {points} vehicles can be charged at once")

def plot_top_operators(df):
    """
    Calculates the top 5 charging station operators based on the total number of charging points ('AnzahlLadepunkteNLL') they operate and generates a horizontal bar plot to visualize the results.
    Args:
        df (pd.DataFrame): The input DataFrame containing weather station data.
    Returns:
        None: Displays the Matplotlib plot directly to the console/notebook output.
    """
    top_operators = (
        df.groupby("Betreiber")["AnzahlLadepunkteNLL"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_operators.values, y=top_operators.index, palette="magma")
    plt.title("Top 5 Charging Station Operators in Germany (Total Vehicles Charged at Once)", fontsize=14)
    plt.xlabel("Total Charging Points")
    plt.ylabel("Operator")
    plt.show()


find_top_operators(df)
plot_top_operators(df)


