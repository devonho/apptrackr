package org.devonho.apptrackr;

import java.io.IOException;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.FirestoreOptions;

@Configuration
@ComponentScan(basePackageClasses =  Firestore.class)
class FireStoreFactory {

  @Bean
  public static Firestore create() {

    try {
      FirestoreOptions firestoreOptions = FirestoreOptions.getDefaultInstance().toBuilder()
          .setProjectId("apptrackr-444905")
          .setCredentials(GoogleCredentials.getApplicationDefault())
          .build();
      Firestore db = firestoreOptions.getService();
      return db;  
    } catch(IOException e) {
      return null;
    }
  }
}

